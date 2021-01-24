# Rails test
```
~/work/cicd >>> docker-compose ps                                                                                                                                                                           [master]
   Name                 Command              State    Ports
-----------------------------------------------------------
cicd_db_1    docker-entrypoint.sh postgres   Exit 0
cicd_web_1   irb                             Exit 1
~/work/cicd >>> docker-compose up -d                                                                                                                                                                        [master]
Starting cicd_db_1 ... done
Starting cicd_web_1 ... done
~/work/cicd >>> docker-compose exec web bash                                                                                                                                                                [master]
root@0da89398a0f6:/product-register# rails test
2021-01-21 12:20:26 WARN Selenium [DEPRECATION] Selenium::WebDriver::Chrome#driver_path= is deprecated. Use Selenium::WebDriver::Chrome::Service#driver_path= instead.
2021-01-21 12:20:30 WARN Selenium [DEPRECATION] Selenium::WebDriver::Chrome#driver_path= is deprecated. Use Selenium::WebDriver::Chrome::Service#driver_path= instead.
Run options: --seed 7426

# Running:

.......

Finished in 4.670591s, 1.4987 runs/s, 1.9270 assertions/s.
7 runs, 9 assertions, 0 failures, 0 errors, 0 skips
root@0da89398a0f6:/product-register#
```