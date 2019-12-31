require 'aws-sdk'

ec2 = Aws::EC2::Resource.new(region: 'ap-northeast-1')

ec2.instances(
        filters: [
#               { name: "instance-state-name", values: ["running"] },
                { name: "instance-type"      , values: ["t2.micro"] }
        ]
).each do |instance|
        tag_name = ""
        instance.tags.each { |tag|
                tag_name = tag.value if tag.key == "Name"
        }

        #puts "#{instance.id} #{tag_name} #{instance.state.name} #{instance.private_ip_address} #{instance.public_ip_address} #{instance.instance_type}"
        puts "#{instance.public_dns_name}"
end
