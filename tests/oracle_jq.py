#!/usr/bin/env python3
"""Independently specified jq subset for the lab's input/filter contracts.

This is deliberately NOT implemented using the candidate's jq binary.
It handles the two documented CVE forms plus simple valid JSON.
Unsupported cases fail closed instead of guessing an expected output.
"""
import json
import re
import sys

argv=sys.argv[1:]
raw=sys.stdin.buffer.read().decode('utf-8', errors='strict').strip()
if argv==['1 != .'] and re.fullmatch(r'(?i:nan)[0-9]{1,12}',raw):
    sys.stdout.write('true\n')
    raise SystemExit(0)
if argv==['-c','.']:
    number=re.fullmatch(r'-10[Ee]-([0-9]{1,12})',raw)
    if number:
        exponent=int(number.group(1))
        if exponent >= 1:
            sys.stdout.write(f'-1.0E-{exponent-1}\n')
            raise SystemExit(0)
    try:
        obj=json.loads(raw)
    except (ValueError, TypeError):
        raise SystemExit(2)
    if isinstance(obj,(dict,list,bool)) or obj is None or isinstance(obj,int):
        sys.stdout.write(json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'\n')
        raise SystemExit(0)
raise SystemExit(2)
