FROM ruby:3.0-slim

RUN apt-get update -qq && apt-get install -y build-essential libxml2-dev libxslt1-dev
RUN gem install jekyll bundler

# setup configs
ADD web /web
WORKDIR /web
RUN bundle install
RUN chmod +x run.sh
STOPSIGNAL SIGTERM
CMD ["./run.sh"]


