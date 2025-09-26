#include <iostream>


// [[Function init, IMPL_CPP_INIT, impl, [R_EXAMPLE_CPP_INIT_ONE, R_EXAMPLE_CPP_INIT_TWO] ]]
void init(){
    // @need-ids: R_EXAMPLE_CPP_INIT_ONE, R_EXAMPLE_CPP_INIT_TWO
    //...
    // @need-ids: R_EXAMPLE_CPP_INIT_TWO
    //...
}

// [[Function evaluate, IMPL_CPP_EVALUATE, impl, [R_EXAMPLE_CPP_EVALUATE_ONE, R_EXAMPLE_CPP_EVALUATE_TWO] ]]
void evaluate(){
    // @need-ids: R_EXAMPLE_CPP_EVALUATE_ONE, R_EXAMPLE_CPP_EVALUATE_TWO
    //...
    // @need-ids: R_EXAMPLE_CPP_EVALUATE_TWO
    //...
}

// [[Function main, IMPL_CPP_MAIN, impl, [R_EXAMPLE_CPP_MAIN_ONE] ]]
int main() {
    init()
    std::cout << "Starting demo:" << std::endl;
    evaluate();
    std::cout << "demo finished." << std::endl;
    return 0;
}
