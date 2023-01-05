#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = list(map(int, input().split()))
snz = False
i = 0
while (i < len(s)):
    if s[i] == 0 and not snz:
        snz = True
        j = i
    while s[i] == 0 and i < len(s) -1:
        i += 1
    if snz and s[i]!= 0:
        s[j],s[i] = s[i], 0
        j += 1
    i += 1
print(*s)




