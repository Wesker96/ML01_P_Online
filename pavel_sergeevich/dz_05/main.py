import pandas

"""
1.	Общее число оценок в файле
2.	Общее количество пользователей, поставивших оценки
3.	Общее количество оцененных фильмов
4.	ID самого активного пользователя
5.	Фильм, собравший наибольшее количество оценок

Выводы: слегка пощупали pandas

"""

path = "ratings_small.csv"

# ['userId', 'movieId', 'rating', 'timestamp']
ratings_df = pandas.read_csv(path)
print(type(ratings_df.rating))

print("Общее число оценок в файле: " + str(len(ratings_df.rating)))
print("Общее количество пользователей: " + str(ratings_df.userId.nunique()))
print("Общее количество оцененных фильмов: " + str(ratings_df.movieId.nunique()))
print("ID самого активного пользователя: " + str(ratings_df.userId.value_counts(sort=True).index[0]))
print("Фильм, собравший наибольшее количество оценок: " + str(ratings_df.movieId.value_counts(sort=True).index[0]))

"""
Out:
Общее число оценок в файле: 100004
Общее количество пользователей: 671
Общее количество оцененных фильмов: 9066
ID самого активного пользователя: 547
Фильм, собравший наибольшее количество оценок: 356
"""

