# IPASSprojectSchaakAlgoritme

Deze repo is voor mijn schaakapplicatie die puzzels kan maken en oplossen door middel van een negamax algortime.
De applicatie kan gebruikt worden om te schaken en je eigen posities op te stellen, die je vervolgens uit kan spelen of aan de computer vragen of er een mat aanwezig is.

Om de applicatie te kunnen runnen heb je alle .py files (op testcases na) in deze repo nodig en de images file. 
Op het moment dat je main.py runt kun je de applicatie gebruiken.

Wanneer je de applicatie gestart hebt:
je kunt een normale schaak pot spelen.
op het moment dat je de 'z' toets klikt maak je een zet ongedaan.
op het moment dat je de 's' toets klikt begint het algoritme de zetten over te nemen.
op het moment dat je de 'a' toets klikt onderbreek je dit.
op het moment dat je de 'r' toets klikt reset je het bord naar een normale schaakpositie.

De reset knop aan de rechterkant van het scherm doet hetzelfde als de 'r' toets.
De builder knop creeërt een leeg bord en activeert builder mode.
de 'check for mate' knop gebruikt het algoritme om in de python terminal te printen of hij een mat kan vinden.

Binnen de builder mode kun je een aantal dingen doen:

  je kunt een schaakstuk selecteren aan de rechterkant van het scherm en deze vervolgens op het bord plaatsen
  (wit gaat altijd van onder naar boven en zwart van boven naar onder).
  
  je kunt de castle rights aanpassen door linksboven of linksonder of rechtsboven of rechtsonder op de 'castle rights' knop te drukken.
  Deze plekken op de knop corresponderen met het bord (linksboven is castlen voor de zwarte koning naar de linker kant).
  
  Je kunt op de knop tussen play en castle rights in klikken om de beginnende kleuren aan te passen
  Wanneer deze kleur wit is, begint wit en andersom.
  
  Je kunt op 'play' klikken om de positie speelbaar te maken.
