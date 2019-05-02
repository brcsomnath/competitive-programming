'''
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}


Solution:
The genius idea: why not combinely use special character and size information. Wrap your string in following way in the encode string.

encode_string = size1:{original_string}size2:{original_string}size3:{original_string}size4:{original_string}

each original string is wrap through following way:
original_string ---> size1:{original_string}
'''