from typing import List
def sanitizeSecrets(text: str) -> str:
    v=''
    x=0
    z=0
    for i in range(len(text)):
        if text[i]=='<':
            x=i
        if text[i]=='>':
            for j in range(i+1 ,len(text)):
                if text[j] =='>':
                    z = j
                    break
            break

    g = ''
    for i in range(x,z+1):
        g+=text[i]

    print(z)
    v = text.replace(g , '[REDACTED]')
    return v

print(sanitizeSecrets("token=<secret>ABC123</secret>; user=admin"))