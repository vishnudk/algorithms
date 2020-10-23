def dateOfProgrammersDay(year):
    if year==1918:
        return(str("26.9.")+str(year))
    if year>=1918:
        if year % 100==0:
            if year%400==0:
                return(str("12.9.")+str(year))
            else:
                return(str("13.9.")+str(year))

        elif year%4==0:
            return(str("12.9.")+str(year))
        else:
            return(str("13.9.")+str(year))

    else:
        if year%4==0:
            return(str("12.9.")+str(year))
        else:
            return(str("13.9.")+str(year))



if __name__ == "__main__":
    dateOfProgrammersDay(2017)