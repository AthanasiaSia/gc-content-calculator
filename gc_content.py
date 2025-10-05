def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    if len(sequence) > 0:
        return (gc_count / len(sequence)) * 100  
    else: 
        0

if __name__ == "__main__":
    print("Enter DNA sequences to calculate GC content (type 'exit' to quit):")
    while True:
        seq = input("DNA sequence: ").strip()
        if seq.lower() == "exit":
            print("Goodbye!")
            break
        gc = calculate_gc_content(seq)
        print(f"GC Content: {gc:.2f}%\n")