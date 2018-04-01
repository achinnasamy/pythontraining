



class ReadTwitterTags:


    def read_twitter_tags(self, file_name):


        all_tags = []

        with open(file_name) as file:

            for l in file:
                all_tags.append(l.strip())

        return all_tags



class DataWriter:

    def __init__(self, _path_to_file_name_):
        self.file_name = _path_to_file_name_


    #
    # Append Data to file
    #
    def appendDataToFile(self, text_to_be_appended):

        with open(self.file_name, "a") as myfile:
            myfile.write(text_to_be_appended.encode('utf-8').strip()+"\n")

        return
