#movie recommendation system
movie_names = ["Dangal","The Shawshank Redemption","Zindagi Na Milegi Dobara","The Avengers","Queen","Forrest Gump","Drishyam","Get Out","Yeh Jawaani Hai Deewani","The Pursuit of Happyness","Dil Chahta Hai","Parasite","Munna Bhai M.B.B.S.","A Star Is Born"]
movie_genres = [
["Drama","Sports","Biography"],
["Drama"],
["Adventure","Comedy","Drama"],
["Action","Sci-Fi","Adventure"],
["Drama","Comedy"],
["Drama","Romance"],
["Thriller","Crime","Drama"],
["Horror","Thriller"],
["Drama","Romance","Comedy"],
["Drama","Biography"],
["Drama","Romance","Comedy"],
["Thriller","Drama"],
["Comedy","Drama"],
["Romance","Drama","Musical"]
]
print("==== Movies ====")
print("world of movies")
print("")
for x in range(len(movie_names)):
	print(x+1,"-",movie_names[x])
print("")
user_movie = input(" Enter a movie you want to watch ")
user_movie = user_movie.lower()
user_movie = user_movie.strip()
# find index of the movie user entered
found_index = -1
for x in range(len(movie_names)):
	if movie_names[x].lower() == user_movie:
		found_index = x
if found_index == -1:
	print("")
	print("hmm couldnt find that movie")
else:
	target_genres = movie_genres[found_index]
	target_name = movie_names[found_index]
	print("")
	print("Since you liked",target_name,", here are some recommendations:")
	print("")
	rec_names = []
	rec_scores = []
	for x in range(len(movie_names)):
		if x == found_index:
			continue
		score = 0
		for g in movie_genres[x]:
			if g in target_genres:
				score = score+1
		if score > 0:
			rec_names.append(movie_names[x])
			rec_scores.append(score)
	# need to sort these based on score, doing it manually
	for a in range(len(rec_scores)):
		for b in range(len(rec_scores)-1):
			if rec_scores[b] < rec_scores[b+1]:
				# swap scores
				temp_score = rec_scores[b]
				rec_scores[b] = rec_scores[b+1]
				rec_scores[b+1] = temp_score
				# swap names too (gotta keep them in sync)
				temp_name = rec_names[b]
				rec_names[b] = rec_names[b+1]
				rec_names[b+1] = temp_name
	if len(rec_names) == 0:
		print("no recommendations found for this one")
	else:
		for x in range(len(rec_names)):
			print("->",rec_names[x],"(score",rec_scores[x],")")
print("")
print("done")
