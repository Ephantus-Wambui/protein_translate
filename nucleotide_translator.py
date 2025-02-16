#!/usr/bin/env python

def translate():
    user_nuc = input("Please paste your sequences here: ")
    user_nuc_upper = user_nuc.upper()
    try:
        codon = {"TTT":"Phe","TCT":"Ser","TAT":"Tyr","TGT":"Cys","TTC":"Phe","TCC":"Ser","TAC":"Tyr","TGC":"Cys","TTA":"Leu","TCA":"Ser","TAA":"Ter","TGA":"Ter",
             "TTG":"Leu","TCG":"Ser","TAG":"Ter","TGG":"Trp","CTT":"Leu","CCT":"Pro","CAT":"His","CGT":"Arg","CTC":"Leu","CCC":"Pro","CAC":"His","CGC":"Arg",
             "CTA":"Leu","CCA":"Pro","CAA":"Gln","CGA":"Arg","CTG":"Leu","CCG":"Pro","CAG":"Gln","CGG":"Arg","ATT":"Ile","ACT":"Thr","AAT":"Asn","AGT":"Ser",
             "ATC":"Ile","ACC":"Thr","AAC":"Asn","AGC":"Ser","ATA":"Ile","ACA":"Thr","AAA":"Lys","AGA":"Arg","ATG":"Met","ACG":"Thr","AAG":"Lys","AGG":"Arg",
             "GTT":"Val","GCT":"Ala","GAT":"Asp","GGT":"Gly","GTC":"Val","GCC":"Ala","GAC":"Asp","GGC":"Gly","GTA":"Val","GCA":"Ala","GAA":"Glu","GGA":"Gly",
             "GTG":"Val","GCG":"Ala","GAG":"Glu", "GGG":"Gly"}

        protein = []
        for i in range(0, len(user_nuc_upper) - 2, 3):
            codon_triplet = user_nuc_upper[i:i+3]
            protein_translate = codon[codon_triplet]
            protein.append(protein_translate)
        print(f"Your protein sequence is {''.join(protein)}")
    except:
        print(f"Check your input: {user_nuc}")

translate()
