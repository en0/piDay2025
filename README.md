# PiDay 2025 

For Pi Day, I wanted to learn more about spigot algorithms and how they work. I started as most do, on Wikipedia, and a simplified example of Spigot that computes the binary expansion of ln(2) using a simplified identity derived from the Taylor series. 

[Spigot Algorithms](https://en.wikipedia.org/wiki/Spigot_algorithm)

After brushing off my brain and getting the ln(2) binary expansion working (I think), I moved on to my express goal of a spigot algorithm for Pi. As it turns out, this was easier because there is WAY  more information out there about this. In fact, one could find countless examples of these formulas all over the internet. I wanted to learn more so I read a few articles but the most useful to me was a paper by Jeremy Gibbons. 

[Unbounded Spigot Algorithms for the Digits of Pi](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf)

You will notice that the algorithm I ended up using can be found on the second-to-last page of his paper, but in Python. The spigot function is a modified version of Gospher's algorithm considering Gibbons' unproven conjecture. I am not the first person to do this and googling around will find many implementations of this algorithm, most of which match what I am using nearly exactly. 

I want to be clear that none of these are my algorithms but they are my code based on interpretations of other people's algorithms and conjectures. 
