from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('trans.txt', num_epochs=20)
textgen.generate_samples(10, [x * 0.1 for x in range(10)])
