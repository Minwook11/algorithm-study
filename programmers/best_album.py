# link : https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    playsDict = {}
    d = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = play
        d[genre] = d.get(genre, []) + [ (play, i) ]

    genreSort = sorted(playsDict.items(), key = lambda x: x[1], reverse = True)

    for (genre, totlaPlay) in genreSort:
        d[genre] = sorted(d[genre], key = lambda x: (-x[0], x[1]))
        answer += [ idx for (play, idx) in d[genre][:2] ]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))