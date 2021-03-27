import logging

logging.basicConfig(level=logging.INFO)

def duplicate_encode(word):
    compare = word.lower()
    encoder = {}
    resp = list(word)
    logging.info(resp)
    for i, j in enumerate(compare):
        logging.info(f'{j}; {i}; {compare[i+1:]}')
        logging.info(f'{encoder.keys()}')
        if (j in compare[i+1:]) or (j in encoder.keys()):
            encoder[j] = ")"
            logging.info(f'{j} adicionado ao dicionario como \')\'')
        else:
            encoder[j] = "("
            logging.info(f'{j} adicionado ao dicionario como \'(\'')
        resp[i] = encoder[j]
        logging.info(resp)
    resp = ''.join(resp)
    return resp
            
x = duplicate_encode("Aas")
print(x)
