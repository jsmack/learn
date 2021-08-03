# Rails

## docker build
```bash
$ mkdir product-register
$ cd product-register
$ touch Gemfile Gemfile.lock
$ docker build .
```

## Run
```bash
$ docker run -it --rm -v ~/work/git/learn/infra/docker/udemy/kame1/084/product-register:/product-register -p 3000:3000 090c1b6d226d bash
```

## docker-compose
```bash
$ docker-compose build
$ docker-compose up -d
$ docker-compose ps
$ docker-compose exec <servicename> bash 
$ docker-compose down # stop and rm
```

## generate rails app
```bash
$ docker-compose exec web  bash
root@094803e27c0a:/product-register# rails new . --force --database=postgresql --skip-bundle
```

## Check Gemfile update

## RUN rails
```bash
root@094803e27c0a:/product-register# rails s -b 0.0.0.0
Could not find gem 'pg (>= 0.18, < 2.0)' in any of the gem sources listed in your Gemfile.
Run `bundle install` to install missing gems.
root@094803e27c0a:/product-register# exit
exit
```

## Stop and rm compose 
```bash
$ docker-compose down
```

## Rebuild and up(detouch)
```bash
$ docker-compose up --build -d
```

## connect
```bash
$ docker-compose exec web bash
```

## Run rails
```bash
$ rails s -b 0.0.0.0
```

## Connect rails
- http://0.0.0.0:3000


## Stop rails
Ctrl + C

## Create database on rails
- Error
```bash
$ rails db:create
could not connect to server: No such file or directory
```

## Edit yaml
- database.yml
### build and up
```bash
$ docker-compose up --build -d
```

## Check docoker volume
```bash
$ docker volume ls                                                               
DRIVER    VOLUME NAME
local     product-register_db-data
$ docker volume inspect product-register_db-data                                   
[
    {
        "CreatedAt": "2021-01-18T13:33:53Z",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.project": "product-register",
            "com.docker.compose.version": "1.27.4",
            "com.docker.compose.volume": "db-data"
        },
        "Mountpoint": "/var/lib/docker/volumes/product-register_db-data/_data",
        "Name": "product-register_db-data",
        "Options": null,
        "Scope": "local"
    }
]
$
```

``` bash
$ docker-compose up -d                
Starting product-register_db_1 ... done
Recreating product-register_web_1 ... done
$ 
$root@986aae4e7786:/product-register# rails db:create
Created database 'product-register_development'
Created database 'product-register_test'
root@986aae4e7786:/product-register#
```


## Create app
```bash
root@986aae4e7786:/product-register# rails g scaffold product name:string price:integer vendor:string
      invoke  active_record
      create    db/migrate/20210118134015_create_products.rb
      create    app/models/product.rb
      invoke    test_unit
      create      test/models/product_test.rb
      create      test/fixtures/products.yml
      invoke  resource_route
       route    resources :products
      invoke  scaffold_controller
      create    app/controllers/products_controller.rb
      invoke    erb
      create      app/views/products
      create      app/views/products/index.html.erb
      create      app/views/products/edit.html.erb
      create      app/views/products/show.html.erb
      create      app/views/products/new.html.erb
      create      app/views/products/_form.html.erb
      invoke    test_unit
      create      test/controllers/products_controller_test.rb
      create      test/system/products_test.rb
      invoke    helper
      create      app/helpers/products_helper.rb
      invoke      test_unit
      invoke    jbuilder
      create      app/views/products/index.json.jbuilder
      create      app/views/products/show.json.jbuilder
      create      app/views/products/_product.json.jbuilder
      invoke  assets
      invoke    coffee
      create      app/assets/javascripts/products.coffee
      invoke    scss
      create      app/assets/stylesheets/products.scss
      invoke  scss
      create    app/assets/stylesheets/scaffolds.scss
root@986aae4e7786:/product-register#
root@986aae4e7786:/product-register# rails db:migrate
== 20210118134015 CreateProducts: migrating ===================================
-- create_table(:products)
   -> 0.0261s
== 20210118134015 CreateProducts: migrated (0.0269s) ==========================

root@986aae4e7786:/product-register#
```

## Run
```bash
root@986aae4e7786:/product-register# rails db:migrate
== 20210118134015 CreateProducts: migrating ===================================
-- create_table(:products)
   -> 0.0261s
== 20210118134015 CreateProducts: migrated (0.0269s) ==========================

root@986aae4e7786:/product-register#
root@986aae4e7786:/product-register#
root@986aae4e7786:/product-register# rails s -b 0.0.0.0
=> Booting Puma
=> Rails 5.2.4.4 application starting in development
=> Run `rails server -h` for more startup options
Puma starting in single mode...
* Version 3.12.6 (ruby 2.5.8-p224), codename: Llamas in Pajamas
* Min threads: 5, max threads: 5
* Environment: development
* Listening on tcp://0.0.0.0:3000
Use Ctrl-C to stop
```

## Access
http://0.0.0.0:3000

## Access
http://0.0.0.0:3000/products


## Edit routes.rb
```ruby
Rails.application.routes.draw do
  root 'products#index' # Add
  resources :products
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
```
