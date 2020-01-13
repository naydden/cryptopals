#!/usr/bin/env python
import codecs
import string


def hex2base64(hexString):
	rawString = codecs.decode(hexString, 'hex');
	b64String = codecs.encode(rawString, 'base64').decode();
	return b64String;

def XOR(b1, b2):
	result = bytearray();
	for b1, b2 in zip(b1, b2):
		result.append(b1 ^ b2);
	return bytes(result);

def challenge1():
	hex_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	base64_STRING = hex2base64(hex_STRING);
	expected_STRING = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n";
	print("Challenge 1", base64_STRING == expected_STRING);

def challenge2():
	hex1 = "1c0111001f010100061a024b53535009181c";
	hex1 = codecs.decode(hex1, 'hex');
	hex2 = "686974207468652062756c6c277320657965";
	hex2 = codecs.decode(hex2, 'hex');
	result = "746865206b696420646f6e277420706c6179";
	calc = codecs.encode(XOR(hex1,hex2), 'hex').decode();
	print("Challenge 2", calc == result);

def challenge3():
	encodedHex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
	hex1 = codecs.decode(encodedHex, 'hex');
	strings = (''.join(chr(num ^ key) for num in hex1) for key in range(256));
	print("challenge 3", max(strings, key=lambda s: s.count(' ')));

def main():
	challenge1();
	challenge2();
	challenge3();

if __name__ == '__main__':
	main()