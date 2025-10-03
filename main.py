import hashlib

texto = "Minha mensagem segura"
dados_em_bytes = texto.encode('utf-8')


# Retorna o hash)como uma string de dígitos hexadecimais.
meu_hash = hashlib.sha256(dados_em_bytes).hexdigest() 


print(f"Meu texto normal: {texto}")
print(f"Meu hash-sha256: {meu_hash}")