from enum import Enum
class ResponseSignal(Enum):
    
    FILE_TYPE_NOT_SUPPORTED="file_type_not_supported"
    FILE_SIZE_EXCEEDED ="file_size_exceeded"
    FILE_UPLOAD_SUCCESS="FILE_UPLOAD_SUCCESS"
    FILE_UPLOAD_FAILED="FILE_UPLOAD_FAILED"
    FILE_VALIDATED_SUCCESS="FILE_VALIDATED_SUCCESS"