design_memo.txt

**Design Memo: Contact Management System**

I chose a hash table for this contact management system because it makes finding contacts faster and easier. Instead of checking every contact one by one, the program uses a person's name to find where their information is stored. This is helpful when there are hundreds of contacts to search through.

I handled collisions by using linked lists. Sometimes two names end up at the same index, so the linked list allows both contacts to be stored without losing information. I also made it so that if a contact is added again with the same name, their phone number gets updated instead of creating a duplicate.

An engineer might choose a hash table over a list when they need to find information quickly. A list can take longer to search because each item may need to be checked. A tree can be useful when information needs to stay organized in a certain order. Overall, this project helped me understand how hash tables work and why they are useful. I also learned that handling collisions correctly is important to make sure contacts can be stored and found without problems.