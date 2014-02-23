def fizzbuzz(values = range(1, 101)):
    output_list = []
    for value in values:
        if (not value % 3) and (not value % 5):
            output_list.append("fizzbuzz")
        elif (not value % 3):
            output_list.append("fizz")
        elif (not value % 5):
            output_list.append("buzz")
        else:
            output_list.append(str(value))

    return output_list

def main():
    print '\n'.join(fizzbuzz())

if __name__ == '__main__':
    main()
