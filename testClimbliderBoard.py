def testClimbLiderBoard(scores,alice):
        uniq=[]
        l=[]
        uniq=list(set(scores))
        uniq.sort(reverse=True)
        # for i in scores:
        #     if i not in uniq:
        #         uniq.append(i)
        #     uniq.sort(reverse=True)
        for i in alice:
            if i in uniq:
                l.append(uniq.index(i)+1)
            else:
                uniq.append(i)
                uniq.sort(reverse=True)
                l.append(uniq.index(i)+1)
                uniq.pop(uniq.index(i))
        return l


if __name__ == "__main__":
    print(testClimbLiderBoard([100,90,90,80,75,60],[50,65,65,77,90,102]))
    