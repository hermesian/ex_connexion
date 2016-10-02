Connexionテスト
===============

Dockerイメージビルド
------------------

::

    $ docker build -t ex_cnx -f Dockerfile .

Dockerコンテナの起動
------------------

::

    $ docker run -d -p 8080:8080 ex_cnx

つかってみる
----------

::

    $ curl -F 'file=@pets_list.yml' http://192.168.99.100:8080/pets
