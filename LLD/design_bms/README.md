Design
Follow up: concurrency. Same ticket is not issue to all


Concurrency Handling
- same seat cannot be assigned to different users
- if user selects a seat - it should be blocked for 10 mins

2 types of Lock
- Optimistic Lock - selected
    Multiple users can read
    user1 on update, also updates the data version 
    user2 for update, matches versions, on fail fetch read

- Pesimistic Lock
    Lock at the time of read only
    blocks read from another user
    released after update only


