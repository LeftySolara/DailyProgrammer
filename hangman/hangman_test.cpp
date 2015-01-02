#include "Hangman.h"
#include "gtest/gtest.h"

#define TEST_WORD "Tailor"

// Test fixture
class Hangman_tests : public testing::Test
{
protected:
    Hangman game = Hangman(TEST_WORD);

    virtual void SetUp() {}
    virtual void TearDown() {}
};

TEST(Hangman_tests, Constructor)
{
    Hangman one = Hangman("hello");
    ASSERT_EQ("hello", one.get_word());

    Hangman two = Hangman("world");
    ASSERT_EQ("world", two.get_word());
}

int main(int argc, char *argv[])
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}