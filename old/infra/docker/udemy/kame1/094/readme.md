# Github 
## Create repository
## Set git config
```
$ git config user.name xxx
$ git config user.email  yyy
```

### Linking my repository with the github repository
```
~/work/cicd >>> git config user.email "jsmackerel@gmail.com"
~/work/cicd >>>
~/work/cicd >>> git remote -v
~/work/cicd >>> git remote add origin https://github.com/jsmack/product-register.git
~/work/cicd >>> git remote -v
origin	https://github.com/xxx/product-register.git (fetch)
origin	https://github.com/xxx/product-register.git (push)
~/work/cicd >>> 
```

### add and commit and push
```
~/work/cicd >>> git add .
~/work/cicd >>> git commit -m"first commit"
[master (root-commit) c53dd76] first commit
 101 files changed, 1753 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 .ruby-version
 create mode 100644 Dockerfile
 create mode 100644 Gemfile
 create mode 100644 Gemfile.lock
 create mode 100644 README.md
 create mode 100644 Rakefile
 create mode 100644 app/assets/config/manifest.js
 create mode 100644 app/assets/images/.keep
 create mode 100644 app/assets/javascripts/application.js
 create mode 100644 app/assets/javascripts/cable.js
 create mode 100644 app/assets/javascripts/channels/.keep
 create mode 100644 app/assets/javascripts/products.coffee
 create mode 100644 app/assets/stylesheets/application.css
 create mode 100644 app/assets/stylesheets/products.scss
 create mode 100644 app/assets/stylesheets/scaffolds.scss
 create mode 100644 app/channels/application_cable/channel.rb
 create mode 100644 app/channels/application_cable/connection.rb
 create mode 100644 app/controllers/application_controller.rb
 create mode 100644 app/controllers/concerns/.keep
 create mode 100644 app/controllers/products_controller.rb
 create mode 100644 app/helpers/application_helper.rb
 create mode 100644 app/helpers/products_helper.rb
 create mode 100644 app/jobs/application_job.rb
 create mode 100644 app/mailers/application_mailer.rb
 create mode 100644 app/models/application_record.rb
 create mode 100644 app/models/concerns/.keep
 create mode 100644 app/models/product.rb
 create mode 100644 app/views/layouts/application.html.erb
 create mode 100644 app/views/layouts/mailer.html.erb
 create mode 100644 app/views/layouts/mailer.text.erb
 create mode 100644 app/views/products/_form.html.erb
 create mode 100644 app/views/products/_product.json.jbuilder
 create mode 100644 app/views/products/edit.html.erb
 create mode 100644 app/views/products/index.html.erb
 create mode 100644 app/views/products/index.json.jbuilder
 create mode 100644 app/views/products/new.html.erb
 create mode 100644 app/views/products/show.html.erb
 create mode 100644 app/views/products/show.json.jbuilder
 create mode 100755 bin/bundle
 create mode 100755 bin/rails
 create mode 100755 bin/rake
 create mode 100755 bin/setup
 create mode 100755 bin/update
 create mode 100755 bin/yarn
 create mode 100644 config.ru
 create mode 100644 config/application.rb
 create mode 100644 config/boot.rb
 create mode 100644 config/cable.yml
 create mode 100644 config/credentials.yml.enc
 create mode 100644 config/database.yml
 create mode 100644 config/environment.rb
 create mode 100644 config/environments/development.rb
 create mode 100644 config/environments/production.rb
 create mode 100644 config/environments/test.rb
 create mode 100644 config/initializers/application_controller_renderer.rb
 create mode 100644 config/initializers/assets.rb
 create mode 100644 config/initializers/backtrace_silencers.rb
 create mode 100644 config/initializers/content_security_policy.rb
 create mode 100644 config/initializers/cookies_serializer.rb
 create mode 100644 config/initializers/filter_parameter_logging.rb
 create mode 100644 config/initializers/inflections.rb
 create mode 100644 config/initializers/mime_types.rb
 create mode 100644 config/initializers/wrap_parameters.rb
 create mode 100644 config/locales/en.yml
 create mode 100644 config/puma.rb
 create mode 100644 config/routes.rb
 create mode 100644 config/spring.rb
 create mode 100644 config/storage.yml
 create mode 100644 db/migrate/20210120135102_create_products.rb
 create mode 100644 db/schema.rb
 create mode 100644 db/seeds.rb
 create mode 100644 docker-compose.yml
 create mode 100644 lib/assets/.keep
 create mode 100644 lib/tasks/.keep
 create mode 100644 log/.keep
 create mode 100644 package.json
 create mode 100644 public/404.html
 create mode 100644 public/422.html
 create mode 100644 public/500.html
 create mode 100644 public/apple-touch-icon-precomposed.png
 create mode 100644 public/apple-touch-icon.png
 create mode 100644 public/favicon.ico
 create mode 100644 public/robots.txt
 create mode 100644 storage/.keep
 create mode 100644 test/application_system_test_case.rb
 create mode 100644 test/controllers/.keep
 create mode 100644 test/controllers/products_controller_test.rb
 create mode 100644 test/fixtures/.keep
 create mode 100644 test/fixtures/files/.keep
 create mode 100644 test/fixtures/products.yml
 create mode 100644 test/helpers/.keep
 create mode 100644 test/integration/.keep
 create mode 100644 test/mailers/.keep
 create mode 100644 test/models/.keep
 create mode 100644 zwtest/models/product_test.rb
 create mode 100644 test/system/.keep
 create mode 100644 test/system/products_test.rb
 create mode 100644 test/test_helper.rb
 create mode 100644 tmp/.keep
 create mode 100644 vendor/.keep
~/work/cicd >>>
~/work/cicd >>> git push origin master
Username for 'https://github.com': xxx
Password for 'https://xxx@github.com':
Enumerating objects: 113, done.
Counting objects: 100% (113/113), done.
Delta compression using up to 4 threads
Compressing objects: 100% (100/100), done.
Writing objects: 100% (113/113), 27.83 KiB | 770.00 KiB/s, done.
Total 113 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/xxxx/product-register.git
 * [new branch]      master -> master
~/work/cicd >>>
```