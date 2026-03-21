def tetracao(base, height):
    if height == 0:
        return "error"
    elif height == 1:
        return base
    

    result = base
    for _ in range(1, height):
        result = base ** result
    return result

def main():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    
    result = tetracao(base, height)
    print(f"The result of {base} tetrated to {height} is: {result}")

if __name__ == "__main__":   
    main()
    
