class Greeter
    attr_accessor :name

    def initialize(names)
        @names = names
    end

    def greet
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("each")
            @names.each do |name|
                puts "Hello, #{name}!"
            end
        else
            puts "Hello, #{@names}!"
        end
    end
end

if __FILE__ == $0
    greetings = Greeter.new(["Jerin", "BS"])

    greetings.greet
end