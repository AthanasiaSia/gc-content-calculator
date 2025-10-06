while True:
    sequence = input("Enter your DNA sequence or exit: ").strip().upper()

    if sequence.lower() == "exit":
        print("Exiting program.")
        break
    
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")

    if len(sequence) > 0:
        gc = (gc_count / len(sequence)) * 100
        print(f"GC content: {gc:.2f}%")
    else:
        print("No sequence provided.")