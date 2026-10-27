
import streamlit as st
from urllib.parse import urlparse
import ipaddress
import re

st.set_page_config(
    page_title="Phishing URL Checker",
    page_icon="🛡️"
)

st.title("🛡️ Phishing URL Awareness Checker")
st.write("Check a URL for common phishing warning signs.")
st.warning("Educational tool only. This cannot guarantee a URL is safe.")

url = st.text_input(
    "Enter a URL",
    placeholder="https://example.com/login"
)

if st.button("Check URL"):
    if not url.strip():
        st.error("Please enter a URL.")
    else:
        value = url.strip()

        if not re.match(r"^https?://", value, re.I):
            value = "https://" + value

        parsed = urlparse(value)
        host = parsed.hostname
        warnings = []

        if not host:
            st.error("Invalid URL. Please check your input.")
        else:
            if len(value) > 100:
                warnings.append("URL is unusually long.")

            if "@" in parsed.netloc:
                warnings.append("URL contains an @ symbol.")

            try:
                ipaddress.ip_address(host)
                warnings.append("Hostname is an IP address.")
            except ValueError:
                pass

            if host.startswith("xn--") or ".xn--" in host:
                warnings.append("Hostname contains punycode.")

            if host.count(".") >= 3:
                warnings.append("URL contains multiple subdomains.")

            keywords = [
                "login", "verify", "account",
                "secure", "update", "password"
            ]

            found = [word for word in keywords if word in value.lower()]
            if found:
                warnings.append(
                    "Suspicious keywords: " + ", ".join(found)
                )

            if parsed.scheme.lower() == "http":
                warnings.append("URL uses HTTP, not HTTPS.")

            st.subheader("Scan Results")

            if warnings:
                st.error("Warning signs detected")
                for item in warnings:
                    st.write("⚠️", item)
            else:
                st.info("No obvious warning signs detected.")

            st.caption(
                "This tool checks URL text only. "
                "It does not visit the website or verify its reputation."
            )
