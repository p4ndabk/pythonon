<?php

    namespace App\Models\Cities;

    use Illuminate\Database\Eloquent\Model;
    use Illuminate\Database\Eloquent\SoftDeletes;

    class MssCities extends Model
    {
        use SoftDeletes;

        protected $table = 'mss_cities';
        protected $softDelete = true;
        protected $primaryKey = 'id';
        public $incrementing = true;
        public $timestamps = false;

        protected static function keyname()
        {
            return (new static())->getKeyName();
        }

        protected static function tablename()
        {
            return (new static())->getTable();
        }

        protected $hidden = ['deleted_at'];
        protected $fillable = ['city',
            'created_at',
            'deleted_at',
            'ibge_code',
            'id',
            'state',
            'updated_at', ];
    }
    