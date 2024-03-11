#contoh 1
stack = ['abdul', 'ilham', 'ijab', 'nurul']
print(stack)
print(stack.pop())
print(stack)
stack.append('putu')
print(stack)

# contoh 2
stack0 = ['abdul', 'ilham', 'ijab', 'nurul']
stack1 = ['iksan', 'jamal', 'ARUL']

new_stack = stack0 + stack1
print(new_stack)

new_stack = stack0 * 2
print(new_stack)

new_stack1 = [*stack0, *stack1]
print(new_stack1)

#contoh 3
stack0 = ['abdul', 'ilham', 'ijab', 'nurul']

print(stack0.pop(1)) # ilham
print(stack0) # [abdul, ijab, nurul]
print(stack0.pop(1)) # ijab
print(stack0) # [abdul, nurul]

#contoh 4
stack0 = ['abdul', 'ilham', 'ijab', 'nurul']

stack0.pop(1)
print(stack0)

stack0.insert(1, 'nurul')
print(stack0)

stack0.pop(3)
stack0.insert(3, 'ilham')
print(stack0)

# contoh 5
stack0 = {'abdul', 'ilham', 'ijab', 'nurul'}
stack0.add('jamal') # nambah data
stack0.remove('ijab') # ijab ilang
# stack.pop() # ilang random
stack0.clear() # ilang semua
print(stack0)

# contoh 5 integer
set = (1, 3, 2, 4, 5)

print(set)

# contoh 6
set1 = {4, 3, 'anjay', 3, 1, 5}
set2 = {6, 7, 8}
set1.add('jamal')
print(set1)
set1.remove('ijab')
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
print(set1.union(set2))
set1.update(set2)
print(set1)

#contoh 7

data_diri = {
    'nama': 'luhut jamal siregar',
    'kelas': 'TI08',
    'hobi': [
        'mancing',
        'nonton',
    ],
    'cita-cita': 'kapal laud',
    'matkul': {
        'senin': 'pemweb',
        'selasa': ['so', 'ddp'],
    }
}

data_diri['nama'] = 'ilham abdullah'
# print()
print(data_diri['nama'])