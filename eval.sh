#!/bin/bash

cd text-detoxification

{ # try

    source eval_env/bin/activate
    export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION='python'
    # python evaluation/evaluate.py -h
    # read -p "Press enter to continue"

    # python evaluation/evaluate.py --submission "../preds/en/4-gram_LOOKBACK_sub.tsv" --reference "../preds/en/4-gram_LOOKBACK_ref.tsv" --device "cpu" && 
    
    for sub_file in ../preds/en/*_sub.tsv; do
        base_name=$(basename "$sub_file" _sub.tsv)
        ref_file="../preds/en/${base_name}_ref.tsv"

        if [[ -f "$ref_file" ]]; then
            echo "Evaluating: $base_name"
            python evaluation/evaluate.py \
                --submission "$sub_file" \
                --reference "$ref_file" \
                --device "cpu" \
                --efficient 1
        else
            echo "Missing reference file for: $base_name"
        fi
    done

    cd ..

} || { # catch
    cd ..
}