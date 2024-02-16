# code 다운로드
if [ -d "../code" ] ; then
	echo "code 디렉토리가 이미 있습니다."
else
	cd ..
    mkdir code
    cd code
	wget wget https://aistages-api-public-prod.s3.amazonaws.com/app/Competitions/000269/data/code.tar.gz
	tar -zxvf code.tar.gz
	rm code.tar.gz
    echo "code 디렉토리에 압축을 풀었습니다."
	cd ../level2-cv-semanticsegmentation-cv-07
fi


# data
if [ -d "../data" ] ; then
	echo "data 디렉토리가 이미 있습니다."
elif [ -e "../data.tar.gz" ]; then
    # data 디렉토리 생성
    cd ..
    mkdir data
    cd data
    # data.tar.gz 압축 해제
    tar -zxvf ../data.tar.gz
    rm ../code.tar.gz
    echo "data 디렉토리에 압축을 풀었습니다."
    cd ../level2-cv-semanticsegmentation-cv-07

else
    echo "data.tar.gz 파일이 존재하지 않습니다."
fi


# git 설정
git config --global commit.template ./.commit_template
git config --global core.editor "code --wait"
echo -e "\e[34mFin git config\e[0m"

# pre-commit 설정
pre-commit autoupdate
pre-commit install
echo -e "\e[34mFin pre-commit\e[0m"

# install requirements
pip install -r ../code/requirements.txt
echo -e "\e[34mFin install requirements\e[0m"

echo -e "\e[34mFin init\e[0m"