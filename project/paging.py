# 게시판 페이징하기
# 게시물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램

# 구조 생각해보기 
# 1. 사용자에게 게시물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력받는다.
# 2. 총 페이지 수를 출력하는 함수인 getTotalPage를 작성한다. 
# 3. 총 페이지 수를 출력한다. 

m, n = map(int, input('게시물 총 건수와 한 페이지에 보여줄 게시물 수를 입력해주세요 : ').split())

def get_total_page(total_post, post_per_page) :
    if total_post % post_per_page == 0 :
        result = total_post // post_per_page
    else :
        result = total_post // post_per_page + 1
    return result

print(f'총 페이지 수는 {get_total_page(m, n)}입니다.')
