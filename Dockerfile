FROM ubuntu:20.04
RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g" /etc/apt/sources.list

# install related libraries
RUN apt update && apt-get install -y ruby-full build-essential zlib1g-dev
RUN gem install jekyll bundler

# setup configs
ADD web /web
WORKDIR /web
RUN chmod +x run.sh
RUN bundle update --bundler
RUN bundle install
STOPSIGNAL SIGTERM
CMD ["/web/run.sh"]


