def calculate_gc_content(sequence):
  sequence = sequence.upper()
  gc_count = sequence.count("G") + sequence.count("C")
  if len(sequence) > 0
    return (gc_count / len(sequence)) * 100  
  else 
    0
  if __name__ == "__main__":
    seq = input("Enter DNA sequence: ").strip()
    gc = calculate_gc_content(seq)
    print(f"GC Content: {gc: .2f}%")
