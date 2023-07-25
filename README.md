## 🎯 Overview
The Parkinson's Keyboard is a specialized keyboard software designed to assist individuals with Parkinson's disease in improving their typing experience. The software aims to reduce the impact of motor skill impairments caused by Parkinson's, making it easier for users to type accurately and efficiently.

The software is designed to be integrated into our custom-made keyboard that runs on a Raspberry Pi Zero.

## 🔑 Key Features
- 💡 Soft Auto-Correction: The embedded software includes an intelligent soft auto-correction mechanism that helps users by blocking erroneous input instead of correcting the word they write, which can be tedious and often ineffective.

- ♿ Accessibility Support: The software is designed with accessibility in mind, making the keyboard a plug-and-play device. All accessibility features run on the keyboard and work with any device it is connected to. This approach avoids reliance on an Operating System to offer accommodations for users with impaired motor skills.

- ⚙️ Responsive Keys: Our keyboard features keycaps that require slightly more force to press and have a significantly lower actuation point compared to standard keyboards. This design prevents accidental input by individuals with Parkinson's disease.

## 💡 How It Works
Please watch this short video showcasing the Parkinson's Keyboard!

[![Video](https://img.youtube.com/vi/Ovz5GyqcyMo/hqdefault.jpg)](https://youtu.be/Ovz5GyqcyMo)

The Parkinson's Keyboard acts as a filter between the human and the computer. As the user types, the keyboard continuously checks the input to ensure it is free of errors and not accidental. It achieves this through word detection and time delays.

The intelligent soft auto-correction feature analyzes the letters being typed and continuously predicts the most likely word being written. If the user inputs a letter that would result in a nonexistent word, the input is blocked as it is likely accidental.

Time delays are used in conjunction with word detection to prevent wrong input. If a user presses a letter too fast, the keyboard blocks the input to prevent tremor-induced actuations. Similarly, if the user is in the process of writing a word, our keyboard adjusts how quickly a letter can be inputted based on the most likely next letter.

## 💥 Complications
During our senior design project, our school shutdown due to COVID-19 cases. As a result, we couldn't fully combine all aspects of our keyboard. The interface for connecting it to a computer and finalizing the PCB-Raspberry Pi Zero-keycaps integration remained unfinished.

Despite these challenges, our team demonstrated resilience and creativity. We are proud of the progress we made and remain committed to realizing the potential of our Parkinson's Keyboard in the future.

## 🙌 Contributors
This project was part of UC Irvine's Senior Design class. The Parkinson's keyboard software and part of its circuit was developed by me, Andres Cervantes.

My teammates included:
- Andrew Wan (Hardware)
- Jacky Liu (Hardware)
- Jeremy Wu (Hardware)

Our faculty advisor for this project was William Tang.

Word list was obtained from [@dwyl](https://github.com/dwyl/english-words)

Special thanks to all contributors for their efforts in creating this innovative solution for individuals with Parkinson's disease.
