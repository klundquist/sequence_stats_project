from Bio.Seq import Seq

sequences = [
    "ATGCGTAACGTT",
    "CGTATGCAT",
    "TTGCAAGGCTA",
    "AGTGCCTAG",
    "ATGCGTRAC"
]

def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    value = round(gc_count / len(seq) * 100, 2)
    return value


def is_valid(seq):
    for base in seq:
        if base not in "ATCG":
            return False
    return True

for s in sequences:
    seq = Seq(s)
    print(f"Sequence {s}")
    print(f"  Length: {len(seq)}")
    print(f"  GC Content: {gc_content(seq)}%")
    print(f"  Valid: {is_valid(seq)}")
    print(f"  Reverse Complement: {seq.reverse_complement()}")
    print("-" * 40)
