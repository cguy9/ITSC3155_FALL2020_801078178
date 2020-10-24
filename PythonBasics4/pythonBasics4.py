# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    if len(emails) > 0:
        i = 0
        for x in contacts:
            contacts[x] = emails[i]
            i += 1
    return contacts

# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE
    if len(contact_info) and len(contact_info[0]) > 0:
        i = 0
        for x in contacts:
            contacts[x] = {"email":contact_info[i][0], "phone": contact_info[i][1]}
            i+=1
    return contacts

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE
    #contactsList [[],[],[]]


    return contactsList

