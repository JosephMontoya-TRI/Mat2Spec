CUDA_VISIBLE_DEVICES=0 python test_Mat2Spec.py \
--concat_comp '' \
--Mat2Spec-loss-type 'KL' \
--label_scaling 'normalized_sum' \
--data_src 'ph_dos_51' \
--trainset_subset_ratio 1.0 \
--Mat2Spec-label-dim 51 \
--Mat2Spec-keep-prob 0.5 \
--batch-size 8
