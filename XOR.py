import base64

class XOR:

    def __init__(self):
        pass


    def Chiffrer_XOR(self, message, clef):
        # Encodage du message en UTF-8
        encoder_message_utf8 = message.encode('utf-8')

        # Conversion de la clef en bytes
        clef_en_bytes = clef.encode('utf-8')

        liste_de_bytes = bytearray()
        for i in range(len(encoder_message_utf8)):
            # Algorithme de chiffrement XOR
            liste_de_bytes.append(encoder_message_utf8[i] ^ clef_en_bytes[i % len(clef_en_bytes)])

        # Encodage en base64
        chiffrer_message = base64.b64encode(liste_de_bytes).decode('utf-8')

        return chiffrer_message
    

    def Dechiffrer_XOR(self, message_chiffre, clef):
        # Décodage du message en base64
        decoder_base64 = base64.b64decode(message_chiffre)

        # Conversion de la clef en bytes
        clef_en_bytes = bytes.fromhex(clef.encode('utf-8').hex())

        liste_de_bytes = bytearray()
        for i in range(len(decoder_base64)):
            # Algorithme de déchiffrement XOR
            liste_de_bytes.append(decoder_base64[i] ^ clef_en_bytes[i % len(clef_en_bytes)])

        try:
            return liste_de_bytes.decode('utf-8')
        
        except UnicodeDecodeError:
            return "Erreur: Impossible de décoder le message"