class Entry:
    def __init__(self, #creates initialisisation function for class and parameters

        # identifiers
        source_app,
        date_time_copied,

        # text data
        character_length,
        line_count,
        word_count,

        # file metadata
        file_name,
        file_extension,
        file_type,
        file_path,
        file_size,

        # image metadata
        width,
        height,

        # behavior
        favourite,
        tags,
        folder,
        exists,
        data,
    ):

        # identifiers
        self.source_app = source_app
        self.date_time_copied = date_time_copied

        # text data
        self.character_length = character_length
        self.line_count = line_count
        self.word_count = word_count

        # file metadata
        self.file_name = file_name
        self.file_extension = file_extension
        self.file_type = file_type
        self.file_path = file_path
        self.file_size = file_size

        # image metadata
        self.width = width
        self.height = height

        # behavior
        self.favourite = favourite
        self.tags = tags if tags is not None else []
        self.folder = folder
        self.exists = exists

        self.data = data