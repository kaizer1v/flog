abcdefghijklmnopqrstuvwxyz
å∫ç∂´ƒ©˙ˆ∆˚¬µ˜øπœ®ß†¨√∑≈¥Ω
•


# Arrays

- `pop` - removes element from the **end**
- `push` - adds an element in the **end**
- `shift` - removes an element from the **beginning**
- `unshift` - adds an element in the **beginning**
- `splice` - (index, count, ...replace_with), also modifies the input arr
- `slice` - (start_index, end_index - 1), doesn't modify the input arr
- `indexOf` - checks if element, if so returns the index number of the first occurance or else a `-1`

```javsacript
// difference between 2 arrays

function diffArray(arr1, arr2) {
  var newArr = [];
  arr1.forEach(function(item) {
    var ind = arr2.indexOf(item)
    if(ind === -1) {
      newArr.push(item)
    } else {
      arr2.splice(ind, 1)
    }
  })
  return newArr.concat(arr2);
}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
```


# BASH commands
`find ./ -type f | grep -l 'MHNS010000282017' Nashik/**/*.json`
find files where text 'MHNS...' exists within all .json and return the filename (-l)

`pip install -r requirements.txt` to install list of packages from a text file.

`sudo -u postgres psql -l` to login into postgres database
