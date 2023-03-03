""" def string():
    a=input('enter a string: ')
    if a[0:]==a[::-1]:
        print(a,'is a palindrome string')
    else:
        print(a,'is not a palindrome string')
string() """
def palindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
		return True

a=palindrome('wow')
print(a)


