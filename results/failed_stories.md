## sad path 1 (C:\Users\Huzaib\AppData\Local\Temp\tmp_5473q87\176c4e0fc59741f2aa112deb3153fd40_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_creator -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy


## sad path 2 (C:\Users\Huzaib\AppData\Local\Temp\tmp_5473q87\176c4e0fc59741f2aa112deb3153fd40_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_creator -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_cheer_up -->


## sad path 3 (C:\Users\Huzaib\AppData\Local\Temp\tmp_5473q87\176c4e0fc59741f2aa112deb3153fd40_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_creator -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_cheer_up -->


