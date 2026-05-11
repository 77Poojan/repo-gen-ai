# repo-gen-ai

# URL Shortener using Base58 Encoding

A simple URL shortener implementation in Python inspired by services like TinyURL and Bitly.

## Features

- Encode long URLs into short URLs
- Decode short URLs back to original URLs
- Uses Base58 encoding for compact URL generation
- Lightweight in-memory storage

## How It Works

1. Every new URL gets a unique integer ID.
2. The integer is converted into a Base58 string.
3. The Base58 key is appended to the base URL.
4. A hashmap stores the mapping between short keys and original URLs.

Example:

https://google.com
↓
https://tinyurl.com/2

## Technologies Used

- Python 3
- HashMap (Dictionary)
- Base58 Encoding

## Run the Project

```bash
python url_shortener.py