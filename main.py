from twilio.rest import Client 



account_sid = '[your account sid]' 
auth_token = '[your auth token]' 
twilio_alloted_whatsapp_number = 'whatsapp:[your twilio alloted whatsapp number with country code] '
your_whatsapp_number = 'whatsapp:[your whatsapp number with country code]'


client = Client(account_sid, auth_token) 
 
 
 
welcome_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body='Hi there, welcome to WhatsApp Sharky Bot',      
                              to=your_whatsapp_number 
                          ) 
                
welcome_emoji = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body='😊',      
                              to=your_whatsapp_number 
                          )

what_i_can_do_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body='I am here to tell you everything about sharks',      
                              to=your_whatsapp_number 
                          ) 
 
shark_emoji = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body='🦈',      
                              to=your_whatsapp_number 
                          ) 

basic_information_messages = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="BASIC INFORMATION ABOUT SHARKS\n\nINTRODUCTION\n\nSharks are a group of elasmobranch fish characterized by a cartilaginous skeleton, five to seven gill slits on the sides of the head, and pectoral fins that are not fused to the head. Modern sharks are classified within the clade Selachimorpha and are the sister group to the rays.\n\nHABITAT\n\nSharks are found from shallow to deep sea environments, in coastal, marine and oceanic environments the world over. Some species inhabit shallow, coastal regions, while others live in deep waters, on the ocean floor and in the open ocean.\n\nLIFE CYCLE\n\nA female white shark gives birth to just five or so “pups” every other year. Their slow reproduction process makes white sharks vulnerable to extinction. Scientists classify white sharks into five different life stages: Pups, Young of the Year, Juveniles, Subadults and Adults.\n\nPREDATORS\n\nGastropods aren't the only organisms known to prey on elasmobranch eggs – other elasmobranchs, bony fishes, seals, whales and even monkeys are known to consume shark and ray eggs.",      
                              to=your_whatsapp_number 
                          )                                                                                                       
fun_fact_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""FUN FACT

* Sharks do not have bones.
 * Most sharks have good eyesight.
* Sharks have special electroreceptor organs.
* Shark skin feels similar to sandpaper.
* Sharks can go into a trance.
* Sharks have been around a very long time.
* Scientists age sharks by counting the rings on their vertebrae.""",      
                              to=your_whatsapp_number 
                          )

best_website_to_learn_about_sharks_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""BEST WEBSITES TO LEARN MORE ABOUT SHARKS

1. https://www.worldwildlife.org/species/shark
2. https://www.sharksider.com/""",      
                              to=your_whatsapp_number 
                          )


best_youtube_videos_to_learn_about_sharks_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""BEST YOUTUBE VIDEOS TO LEARN MORE ABOUT SHARKS

1. https://youtu.be/4HGNqFdaD34
2. https://youtu.be/cHaNCVJ5Ko0
3. https://youtu.be/t82m6vPhsEA
4. https://youtu.be/rG4jSz_2HDY
5. https://youtu.be/O2FInaOCqoo""",      
                              to=your_whatsapp_number 
                          )



best_shark_games_to_play_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""BEST SHARK GAMES TO PLAY

1. Sea Fishing - fun toddler and kids games for free!
Link - https://play.google.com/store/apps/details?id=com.artal.fishing.game.android

2. Pinkfong Baby Shark Phone
Link - https://play.google.com/store/apps/details?id=kr.co.smartstudy.singingphone_android_googlemarket

3. Baby Shark Jigsaw Puzzle Fun
Link - https://play.google.com/store/apps/details?id=kr.co.smartstudy.kidspuzzlefun_android_googlemarketo""",      
                              to=your_whatsapp_number 
                          )
                          
                          
buy_your_blahaj_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""Buy your Blahaj from amazon
Link - https://www.amazon.in/Ikea-BLAHAJ-Soft-Toy-Shark/dp/B07S7PBDNG""",      
                              to=your_whatsapp_number 
                          )   
 
                                                 
previous_year_sharkhacks_hackathon_winners_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""VIEW PROJECTS OF PREVIOUS YEAR'S SHARKHACKS HACKATHON WINNERS ON DEVPOST

1. Blahajack
Link - https://devpost.com/software/blahaj

2. BLÅHAJ THE BRAVEHEART
Link - https://devpost.com/software/blahaj-the-braveheart

3. SharkRank
Link - https://devpost.com/software/sharkrank

4. Filter Frenzy
Link - https://devpost.com/software/filter-frenzy

5. GitMeToTheBLÅHAJ
Link - https://devpost.com/software/gitmetotheblahaj

6. Save the BLAHAJ
Link - https://devpost.com/software/save-the-shark

7. Carl, Defender of Waves
Link - https://devpost.com/software/carl-defender-of-waves

8. Blalalalahaj
Link - https://devpost.com/software/blalalalahaj

9. Which Shark Are You?
Link - https://devpost.com/software/which-shark-are-you

10. Giddy Shark
Link - https://devpost.com/software/giddy-shark

11. SEAcurity
Link - https://devpost.com/software/seacurity

12. SharkMusicBox
Link - https://devpost.com/software/sharkmusicbox

13. The Phobia
Link - https://devpost.com/software/the-phobia

14. Sharkroom
Link - https://devpost.com/software/sharkroom""",      
                              to=your_whatsapp_number 
                          )                                                                                                           
goodbye_message = client.messages.create( 
                              from_=twilio_alloted_whatsapp_number,  
                              body="""I hope that you liked my content 😊

Your 🦈 WhatsApp Bot""",      
                              to=your_whatsapp_number 
                          )                                                                                       