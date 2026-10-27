# Test Samples — Phishing URL Awareness Checker

| # | Sample URL | Expected result |
|---|---|---|
| 1 | `http://192.0.2.10/account` | IP address warning and HTTP warning |
| 2 | `http://example.com@sample.invalid/login` | @ symbol warning and HTTP warning |
| 3 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments warning |
| 4 | `https://xn--example.invalid/` | Punycode warning |
| 5 | `https://www.example.com/login` | No listed warning signs; this does not prove safety |

## Safety Note

The checker inspects URL text only. It does not open URLs or prove that a URL is safe.